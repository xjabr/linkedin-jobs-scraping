import requests

from bs4 import BeautifulSoup
from time import sleep

from utils import progress
from config import LINKEDIN_JOB_LINK_LIST, LINKEDIN_SINGLE_JOB


class LinkedInJobs(object):
  ids = []
  jobs_info = []
  failed_jobs_id = []
  

  def __init__(self, params = {}):
    self.params = params
    
    if self.fetch_ids():
      self.start_fetching()
      return self.jobs_info, self.failed_jobs_id

    print("Error on fetching jobs id")
    return None, None


  def fetch_ids(self):
    i = 0
    start = 25

    while True:
      list_html = self.__get_list_jobs__(
        {
          **self.params,
          'start': start * i
        }
      )

      if list_html == False:
        break

      page_scapped = BeautifulSoup(list_html, 'html.parser')
      list_jobs = page_scapped.find_all('li')

      progress(0, len(list_jobs), 'Fetching all jobs from LinkedIn...')

      for key, item in enumerate(list_jobs):
        progress(key + 1, len(list_jobs), 'Fetching all jobs from LinkedIn...')

        ent_data = item.find('div').get('data-entity-urn') if item.find('div').get('data-entity-urn') != None else item.find('a').get('data-entity-urn')
        self.ids.append(str(ent_data).split(':').pop())

        sleep(0.1)
      
      i = i + 1

    print(f'\n\nList of all ids found ({len(self.ids)}): ')
    for id in self.ids: print(f' - {id}')
    print('\n')

    return True


  def start_fetching(self):
    for id in self.ids:
      single_job = self.__get_job_by_id__(id)

      # when function return the result check if it have found a job by the id passed as param
      # if single_job isn't false get the data as title, agency name, location and description with bs4
      if single_job != False:
        single_job = BeautifulSoup(single_job, 'html.parser')

        try:
          # append a dict to jobs_info array
          # in this dict are stored the job's id, title, agency name, location and description
          self.jobs_info.append(
            {
              'job_id': id,
              'title': single_job.find('h1', { 'class': 'topcard__title' }).text,
              'agency': single_job.find('a', { 'class': 'topcard__org-name-link' }).text,
              'location': single_job.find('span', { 'class': 'topcard__flavor topcard__flavor--bullet' }).text,
              'description': single_job.find('div', { 'class': 'show-more-less-html__markup' }).text
            }
          )

          print(f'New job found! N. Jobs: {len(self.jobs_info)}')
        except:
          print(f'Fetching data for job id {id} failed.')
          self.failed_jobs_id.append(id)


  def get_jobs(self):
    return self.jobs_info, self.failed_jobs_id


  def __get_list_jobs__(self, params: dict) -> str:
    req = requests.get(LINKEDIN_JOB_LINK_LIST, params)

    if req.status_code != 200:
      # raise Exception('Status Code not equals to 200')
      return False

    return req.text


  def __get_job_by_id__(self, id: dict) -> str:
    req = requests.get(f'{LINKEDIN_SINGLE_JOB}/{id}', {})

    if req.status_code != 200:
      # raise Exception('Status Code not equals to 200')
      return False

    return req.text