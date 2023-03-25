# build_files.sh
pip install pip --no-cache-dir -U
pip install -r requirements.txt --no-cache-dir -U
python3.10 manage.py collectstatic --noinput