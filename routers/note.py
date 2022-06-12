from fastapi import APIRouter, Body, status, Depends
from datetime import datetime
from models.note import Note
from typing import List
from database.mongodb_helper import Database

router = APIRouter()
db = Database()
notes_collection = 'Notes'


@router.post('/notes', response_description='Create a new note')
async def create_note(note: Note):
    note = dict(note)
    ack = await db.insert_document(notes_collection, note)
    return ack


@router.put('/notes/{noteId}', response_description='Update entire note', response_model=Note)
async def update_note(noteId: str):
    pass


@router.patch('/notes/{noteId}', response_description='Update partial note', response_model=Note)
async def update_partial_note(noteId: str):
    pass


@router.delete('/notes/{noteId}', response_description='Delete specific note', response_model=Note)
async def delete_note(noteId: str):
    pass


@router.delete('/notes', response_description='Delete multiple notes', response_model=List[Note])
async def delete_notes():
    pass


@router.get('/notes', response_description='Get all notes', response_model=List[Note])
async def get_all_notes():
    pass


@router.get('/notes/{noteId}', response_description='Get specific note', response_model=Note)
async def get_note(noteId: str):
    pass
