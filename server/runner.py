import uvicorn
from src.main import app


if __name__ == '__main__':
	uvicorn.run(app, host="localhost", port=3002)