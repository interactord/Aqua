docker buildx build --platform linux/amd64 -t asia-northeast3-docker.pkg.dev/livetranslation-ccdc0/my-repo/flask-uvicorn-app:latest .

docker push asia-northeast3-docker.pkg.dev/livetranslation-ccdc0/my-repo/flask-uvicorn-app:latest

gcloud run deploy flask-uvicorn-service \
  --image asia-northeast3-docker.pkg.dev/livetranslation-ccdc0/my-repo/flask-uvicorn-app:latest \
  --platform managed \
  --region asia-northeast3 \
  --allow-unauthenticated