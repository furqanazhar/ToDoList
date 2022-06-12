import sys

from fastapi import APIRouter, Body, status, Depends
from fastapi.responses import JSONResponse
from datetime import datetime
from models.note import Note
from utils.common import convert_response_to_json
from typing import List
from database.mongodb_helper import Database
import json
import traceback

router = APIRouter()
db = Database()
notes_collection = 'Notes'


@router.post('/notes', response_description='Create a new note')
async def create_note(note: Note):
    try:
        note = dict(note)
        data = await db.insert_document(notes_collection, note)
        payload = {
            'message': 'Successfully created resource',
            'data': convert_response_to_json(data)
        }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to create resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)


@router.put('/notes/{noteId}', response_description='Update entire note', response_model=Note)
async def update_note(note_id: str):
    pass


@router.patch('/notes/{noteId}', response_description='Update partial note', response_model=Note)
async def update_partial_note(note_id: str):
    pass


@router.delete('/notes/{noteId}', response_description='Delete specific note', response_model=Note)
async def delete_note(note_id: str):
    pass


@router.delete('/notes', response_description='Delete multiple notes', response_model=List[Note])
async def delete_notes():
    pass


@router.get('/notes', response_description='Get all notes', response_model=List[Note])
async def get_all_notes():
    pass


@router.get('/notes/{noteId}', response_description='Get specific note', response_model=Note)
async def get_note(note_id: str):
    pass
