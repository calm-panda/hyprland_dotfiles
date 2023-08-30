import numpy as np
import pandas as pd
import json
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

app = FastAPI()

# To Check Alistipes_putredinis LiJ_2017__H3M414933__bin.14

# global vars
ABS_PATH = "./DATA_SG"

# helper function
def fileItr(path: str):
    with open(path) as file:
        yield from file

# Genome ID (tsv's)

# Base Models definations
class SpeciesList(BaseModel):
    species: list[str]

class GenomeFilesList(BaseModel):
    file_names: list[str]


@app.post("/getGenomeIDs/")
async def getGenomeFileNames(species_names: SpeciesList):
    res = {}
    df = pd.read_csv(f"{ABS_PATH}/annotation_files_metadata.csv", header=None)
    grouped_metadata = df.groupby(df.columns[1]).agg(list).to_dict()[0]
    for species_name in species_names:
        genome_names =  grouped_metadata.get(species_names)
        if (genome_names!=None) 
        # res[species_names] = 
    return []
    # return StreamingResponse( fileItr(f"{ABS_PATH}/annotation_files_metadata"), media_type="text/csv")

@app.get("/annotation/{file_name}")
async def get(file_name: str):
    return {"message": file_name}


if __name__ == "__main__":
    df = pd.read_csv(f"{ABS_PATH}/annotation_files_metadata.csv", header=None)
    # for i in range(0):
    # print(df)
    print(json.dumps([]==None, indent=4))
