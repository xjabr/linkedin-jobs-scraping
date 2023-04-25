# Params list
# keywords -> string
# location -> string
# distance -> number (km)
# f_TPR (published at) -> pick one of this
# - r + (3600 * 24)       - last 24 hours
# - r + (3600 * 24) * 7   - last week
# - r + (3600 * 24) * 31  - last month
# f_E (level of experience) -> pick on of this
# - 1 Stage
# - 2 Esperienza minima
# - 3 Livello medio
# - 4 Livello medio-alto
# - 5 Direttore
# - 6 Executive
# f_C (agency) -> AGENCY_ID
# f_JT (type of work)
# - F Full time
# - P Part time
# - C Contract
# - T Temporary
# - I Stage
# - O Other
# start -> number (every 25 on linkedin)

LINKEDIN_JOB_LINK_LIST = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search/'
LINKEDIN_SINGLE_JOB = 'https://www.linkedin.com/jobs/view'

FROM_KEY_TO_NAME = dict(
  geoId = 'Geolocation ID',
  keywords = 'Keywords',
  location = 'Location',
  distance = 'Distance',
  f_TPR = 'Published at',
  f_E = 'Level of experience',
  f_C = 'Agency',
  f_JT = 'Type of work',
  f_WT = 'On Site / Remote / Ibrid',
  start = 'Start',
)