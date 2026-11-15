# LLM Inference Topology (English edition)

> **English edition** of [llm-inference-topology](https://github.com/DeconstructorGnostico/llm-inference-topology) (Spanish original, unchanged). Version **0.1.0**, translated from the latest local version on 2026-11-15. Code identifiers, enum values (`ALLOW` / `BLOCK` / `QUARANTINE` / `UNDETERMINED`), messages, comments and docs are in English; the docs were machine-translated and reviewed, so some phrasing may read literally. See [TRANSLATION.md](TRANSLATION.md) for what stays in Spanish by design.

Experimental framework to represent and audit operational systems topologies LLM.

## State

v0.1.0 — executable prototype.

The repository began as a five-level conceptual framework and now contains minimal reproducible implementation.

## Architecture

L4 ─ Application / Interface ↓ L3 ─ Context / Orchestration ↓ L2 ─ Policy / Control ↓ L1 ─ Model Inference ↓ L0 ─ Compute Substrate

## L0 — Compute Substrate

Hardware, memory, network and computing resources used to execute the inference.

## L1 — Model Inference

Implementation of the model:

- Transformer;
- attention;
- decoding;
- embeddings;
- related operations.

## L2 — Policy / Control

It may include:

- system instructions;
- implementation policies;
- filters;
- sorters;
- middleware;
- security mechanisms;
- restrictions arising from training.

These mechanisms do not necessarily belong to the same component nor are they present in all systems.

## L3 — Context / Orchestration

It may include:

- context management;
- meetings;
- performance memory;
- routing;
- scheduling;
- Pipeline coordination.

## L4 — Application / Interface

Application that receives the application and presents the result.

## Context Management

FIFO is not assumed as a universal mechanism.

It may include:

- truncation;
- eviction;
- KV-cache;
- prefix caching;
- paged memory;
- external storage;
- specific mechanisms of runtime.

## Pipeline

INPUT ↓ INTENT ↓ CONTEXT ↓ CONTROL ↓ INFERENCE ↓ VALIDATION ↓ OUTPUT

Formally:

O = V(M(P(C(I(X)))))

Where:

X = input

I = representation of intention

Context C = construcción/gestión

P = política/control

M = model inference

V = validation

O = output

The expression represents the software pipeline and does not literally purport to describe all the internal operations of a Transformer.

## Three dimensions of topology

The concept must distinguish:

COMPUTATIONAL TOPOLOGY hardware / GPU / CPU / memory / network

INFERENCE TOPOLOGY context / model / decoding / pipeline

SYSTEM TOPOLOGY servicios / API / routing / frontend

Initial implementation focuses on operational topology of inference.

## Run

python -m experiments.baseline

## Runner

Python -m topology.parser \ "Analyzes this architecture."

## Show topology

python -m topology.parser --topology

## Ollama

ollama list

python -m topology.parser \ --backend pot \ --model call3.2 \ "Explains the topology of inference."

## Tests

python -m pytest

## Metrics

The initial implementation allows you to record the following: • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

- latency;
- entry tokens;
- exit tokens;
- throughput;
- validation errors.

## Scope

This project is not currently intended to be:

- a new Transformer;
- an engine GPU;
- a training system;
- a replacement of Ollama;
- a flame.cpp replacement;
- a replacement of vLLM;
- a SGLang replacement.

It is an experimental layer to represent, execute and measure an inference topology.
