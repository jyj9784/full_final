name: ci-cd-pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [14.x]
        # See supported Node.js release schedule at https://nodejs.org/en/about/releases/
        
    steps:
      - uses: actions/checkout@v2
      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v2
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      - run: npm install
      - run: npm run build --if-present
#       - run: npm test
#     env:
#       DB_NAME: ${{ secrets.DB_NAME }}
#       CLIENT_ID: ${{ secrets.CLIENT_ID }}
#       COOKIE_SECRET: ${{ secrets.COOKIE_SECRET }}
#       NAVER_ID: ${{ secrets.NAVER_ID }}
#       NAVER_SECRET: ${{ secrets.NAVER_SECRET }}
#       SECRET_KEY: ${{ secrets.SECRET_KEY }}
#       YOUR_CLIENT_ID: ${{ secrets.YOUR_CLIENT_ID }}
#       YOUR_CLIENT_SECRET: ${{ secrets.YOUR_CLIENT_SECRET }}
#       PASSWORD: ${{ secrets.PASSWORD }}
#       ACCESSKEYID: ${{ secrets.ACCESSKEYID }}
#       SECRETACCESSKEY: ${{ secrets.SECRETACCESSKEY }}
#       PORT: ${{ secrets.PORT }}
  
#   build-image:
#     needs: build
#     runs-on: ubuntu-latest
#     steps:
#       - name: Set up QEMU
#         uses: docker/setup-qemu-action@v1
#       - name: Set up Docker Buildx
#         uses: docker/setup-buildx-action@v1
#       - name: Login to DockerHub
#         uses: docker/login-action@v1
#         with:
#           username: ${{ secrets.DOCKERHUB_USERNAME }}
#           password: ${{ secrets.DOCKERHUB_TOKEN }}
#       - name: Build and push
#         id: docker_build
#         uses: docker/build-push-action@v2
#         with:
#           push: true
#           tags: ${{ secrets.DOCKERHUB_USERNAME }}/docker-team:latest
#       - name: Image digest
#         run: echo ${{ steps.docker_build.outputs.digest }}
  dockerPush_AND_deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ubuntu
          key: ${{ secrets.PRIVATE_KEY }}
          port: 22
          script: |
            cd /home/ubuntu/the-Final-TeamNote
            git config --global --add safe.directory /home/ubuntu/the-Final-TeamNote
            git pull origin main
            docker rm -f $(docker ps -qa)
            docker rmi -f $(docker images -q) 
            docker-compose up -d --build
