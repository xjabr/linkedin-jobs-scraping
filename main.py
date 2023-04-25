# Author: Gabriele Lanzafame

import config
from linkedin import LinkedInJobs

params = {
  'geoId': '103350119',
  'keywords': input('Keyword: '),
  'location': input('Location: '),
  'f_WT': '2'
}

print('Params:')
for key in params.keys():
  print(f' - {config.FROM_KEY_TO_NAME[key]}: {params[key]}')

jobs, failed = LinkedInJobs()

# filter the jobs by the interests of the client
# read vars for search on input/includes.txt and to exclude from input/excludes.txt
f_vars = open('input/includes.txt', 'r')
e_vars = open('input/excludes.txt', 'r')

includes = f_vars.read().splitlines()
excludes = e_vars.read().splitlines()
type_work = 'remote'

print(f'Jobs Fetched ({len(jobs)})')
print('Wait...')
filtered_jobs = []

# for all jobs in the array check if they're allowd to be added in the filtered_jobs
for item in jobs:
  if not any(e in str(item['description']).lower() for e in excludes) and any(i in str(item['description']).lower() for i in includes) and type_work in str(item['description']).lower():
    filtered_jobs.append(item)

# generate urls for the jobs and urls for jobs that have failed the fetch process
urls = [ str(str(config.LINKEDIN_SINGLE_JOB) + str(item['job_id'])) for item in filtered_jobs ]
urls_failed = [ str(str(config.LINKEDIN_SINGLE_JOB) + value) for value in failed ]

print('Write urls to output/links.txt')
out_file = open('output/links.txt', 'w')
for url in urls: out_file.write(url + '\n')
out_file.close()

failed_file = open('output/failed.txt', 'w')
for url in urls_failed: failed_file.write(url + '\n')
failed_file.close()

print(f'Total jobs founds: {len(filtered_jobs)}')