# Sift: A Distributed Geospatial Feature Segmentation Service

**Sift** is a modular backend framework designed for the automated semantic segmentation of high-resolution geophysical imagery. By abstracting the inference lifecycle into a containerized microservice, Sift enables the extraction of geological features—such as outcrops, mineral veins, and fracture networks—from large-scale geospatial datasets at low latency.

## 1. Project Overview & Structure

The system is architected around a **Separation of Concerns (SoC)**, decoupling data ingestion from the deep learning inference engine. This allows for independent scaling of the API layer and the computational backend.

### Core Architecture

* **Ingestion Pipeline:** Implements a sliding-window tiling strategy to process high-resolution GeoTIFFs that exceed VRAM capacity.
* **Inference Engine:** Utilizes a **U-Net** architecture with a **MobileNetV2** encoder. This configuration provides an optimal trade-off between spatial resolution (via skip connections) and computational efficiency (via depthwise separable convolutions).
* **API Interface:** An asynchronous RESTful interface that handles multi-part binary data, facilitating integration with distributed GIS dashboards.

### Repository Structure

```text
sift/
├── api/                # FastAPI application and endpoint definitions
├── engine/             # PyTorch model architecture and weights
├── processing/         # OpenCV-based tiling and normalization logic
├── tests/              # Unit tests for spatial transforms and model IO
├── Dockerfile          # Multi-stage build for production-ready images
└── main.py             # Application entry point

```

## 2. Technical Stack & Future Expansions

### Current Stack

* **Machine Learning:** PyTorch for model definition and inference; NumPy for tensor manipulation.
* **Computer Vision:** OpenCV (cv2) for spatial pre-processing and coordinate-aligned tiling.
* **Backend:** FastAPI utilized for its asynchronous event loop and Pydantic-based type safety.
* **Infrastructure:** Dockerized environment ensuring deterministic execution across heterogeneous CPU environments.

### Research-Oriented Expansions

* **Geospatial Consistency:** Implementation of a **Weighted Overlap Selection** algorithm to mitigate artifacts at the edges of image tiles during reconstruction.
* **Asynchronous Processing:** Transitioning to a task-queue architecture using **Celery and Redis** to handle "city-scale" batch inference without blocking the main API thread.
* **Quantization:** Leveraging **INT8 Quantization** to optimize inference throughput specifically for CPU-only cloud deployments, reducing memory bandwidth bottlenecks.

## 3. Deployment & Execution

Sift is containerized to ensure environmental parity between development and production. The current implementation is optimized for x86_64 CPU architectures.

### Local Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/your-username/sift.git
cd sift

```


2. **Containerized Execution:**
Build and instantiate the service using Docker. This encapsulates all dependencies including PyTorch and OpenCV.
```bash
docker build -t sift-service .
docker run -p 8000:8000 sift-service

```



### API Interaction

Upon execution, the service exposes an interactive OpenAPI (Swagger) interface at `http://localhost:8000/docs`.

To perform inference on a geological sample:

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@sample_outcrop.tif'

```

---
