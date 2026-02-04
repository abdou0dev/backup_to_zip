from pathlib import Path
import logging, os, zipfile
logging.basicConfig(filename='backup_to_zip.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('--------------------- Start of script ----------------------')
def backup_to_zip(folder):
	folder = Path(folder)

	# Figuring out the name of the backup
	num = 1
	while True:
		logging.info(f'num = {num}')
		zip_filename = Path(folder.stem + '_' + str(num) + '.zip')
		if not zip_filename.exists():
			logging.info(f'new num found: {num}')
			break
		num += 1

	# Creating backup
	print('Creating backup file...')
	with zipfile.ZipFile(folder.parent/zip_filename, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
		print('Adding files...')
		for current_dir, sub_dirs, files in os.walk(folder):
			for file in files:
				file_path = Path(current_dir) / file
				print(f'Adding {file} to backup...')
				zipf.write(file_path, arcname=file_path.relative_to(folder))
		print('Done.')


backup_to_zip(Path.cwd())