# Chautha Mic

Semantic search and retrieval system for the Teen Taal podcast archive.

## Features

* Semantic episode search
* Related episode recommendations
* FastAPI REST API
* Qdrant Cloud vector database
* multilingual-e5-base embeddings
* Swagger documentation

## Tech Stack

* Python
* FastAPI
* Qdrant
* Sentence Transformers
* multilingual-e5-base
* HuggingFace Transformers

## Current Project Status

### Phase 1 — Data Engineering Foundation

* Transcript collection
* Transcript cleaning
* Chunk generation
* Metadata generation

### Phase 2 — Semantic Search Infrastructure

* Vector embeddings
* Qdrant indexing
* Episode search
* Related episode engine
* FastAPI backend

### Phase 3 — Retrieval Augmented Generation (Upcoming)

* Conversational search
* Context retrieval
* LLM answer generation

## API Endpoints

GET /

GET /search

GET /episodes

GET /episode/{episode_id}

GET /related/{episode_id}
