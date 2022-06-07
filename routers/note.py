from fastapi import APIRouter, Body, status, Depends
from datetime import datetime
from models.note import Note
from typing import List


router = APIRouter()


router.post('/note', response_description = 'Create a new note', response_model = Note)
async def create_note():
    pass


router.put('/note', response_description = 'Update entire note', response_model = Note)
async def update_note():
    pass


router.patch('/note', response_description='Update partial note', response_model= Note)
async def update_partial_note():
    pass


router.delete('/note', response_description='Delete note', response_model = Note)
async def delete_note():
    pass


router.delete('/notes', response_description='Delete multiple notes', response_model = List[Note])
async def delete_notes():
    pass


router.get('/notes', response_description='Get all notes', response_model=List[Note])
async def get_all_notes():
    pass


router.get('/notes/{note_id}', response_description='Get note', response_model=Note)
async def get_note(note_id: str):
    pass
