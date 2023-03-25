# build_files.sh
pip install pip wheel --no-cache-dir -U
pip install -r requirements.txt --no-cache-dir -U
python3.9 manage.py collectstatic --noinput