===========
AWS Cement
===========

S3 Commands:
  python bin/s3interface count --key_id ENTER_KEY_HERE --access_key ENTER_SECRET_HERE --bucket S3_BUCKET --dir S3_DIRECTORY
  python bin/s3interface list --key_id ENTER_KEY_HERE --access_key ENTER_SECRET_HERE --bucket S3_BUCKET --dir S3_DIRECTORY
  python bin/s3interface download --key_id ENTER_KEY_HERE --access_key ENTER_SECRET_HERE --bucket S3_BUCKET --dir S3_DIRECTORY --filename FILENAME
  python bin/s3interface upload --key_id ENTER_KEY_HERE --access_key ENTER_SECRET_HERE --bucket S3_BUCKET --dir S3_DIRECTORY--filename PATH/TO/FILENAME
