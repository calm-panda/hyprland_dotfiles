import io
import zipfile
from os import path
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
# Just for dev env
import json

app = FastAPI()

# global vars
ABS_PATH = "./DATA_SG"

# helper function
def fileItr(path: str):
    with open(path) as file:
        yield from file

####################
# Genome ID (tsv's)#
####################
@app.post("/getGenomeIDs/")
async def getGenomeFileNames(species_names: list[str]):

    # Get genome id file names for given species
    res = {}
    df = pd.read_csv(f"{ABS_PATH}/annotation_files_metadata.csv", header=None)
    grouped_metadata = df.groupby(df.columns[1]).agg(list).to_dict()[df.columns[0]]

    # Create response body
    for species_name in species_names:
        genome_names =  grouped_metadata.get(species_name)
        res[species_name] = genome_names if genome_names!=None else []
    return res


@app.post("/annotationZip/")
async def getTsvZip(file_names: list[str]):

    # Create new metadat from user input
    metadata_csv = pd.read_csv(f"{ABS_PATH}/annotation_files_metadata.csv", header=None)
    metadata_csv = metadata_csv.rename({metadata_csv.columns[0]: "genome_ID"}, axis=1)
    new_metadata = pd.merge(pd.DataFrame({"genome_ID": file_names}), metadata_csv, on=["genome_ID"])
    metadata_dict = new_metadata.groupby(new_metadata.columns[1]).agg(list).to_dict()[metadata_csv.columns[0]]

    # Save from the aquired metadata
    buffer = io.BytesIO()
    zf = zipfile.ZipFile(buffer, mode='w')
    for species, genome_id_list in metadata_dict.items():
        for genome_id in genome_id_list:
            genome_file_path = f"{ABS_PATH}/annotation_files/{genome_id}.annotations.tsv"
            if (path.exists(genome_file_path)):
                zf.write(f"{ABS_PATH}/annotation_files/{genome_id}.annotations.tsv", f"{species}/{genome_id}.annotations.tsv")
    zf.close()

    # Send the zip back to user
    return StreamingResponse(
        iter([buffer.getvalue()]), 
        media_type="application/x-zip-compressed",
        headers = {"Content-Disposition":f"attachment;filename=annotations.zip",
                   "Content-Length": str(buffer.getbuffer().nbytes)})


# if __name__ == "__main__":
