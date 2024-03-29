import argparse
import uvicorn
from tests.server.wsgi import run as run_wsgi

args = argparse.ArgumentParser()
args.add_argument("--type", action="store", type=str, default="wsgi")

args = args.parse_args()


if __name__ == "__main__":
  if args.type == "wsgi":
    run_wsgi()
  else:
    uvicorn.run("tests.server.asgi:app", host="0.0.0.0", reload=True, port=8081)