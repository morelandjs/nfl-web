# clear cache and copy static assets

rm -rf website/build
mkdir website/build
cp -r website/static website/build/static

# turn markdown files into templates

python3 -m website.compile