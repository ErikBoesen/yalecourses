import requests


class Course(dict):
    def __init__(self, raw):
        """
        for key in raw:
            # Vet out values that are randomly empty arrays
            if raw[key] == []:
                raw[key] = None
        """
        self.update(raw)
        self.update(self.__dict__)

        print(raw['instructorList'])



class YaleCourses:
    API_TARGET = 'https://gw.its.yale.edu/soa-gateway/course/webservice/index'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get(self, params: dict = {}):
        """
        Make a GET request to the API.

        :param params: dictionary of custom params to add to request.
        """
        params.update({
            'apikey': self.api_key,
            'mode': 'json',
        })
        print(params)
        request = requests.get(self.API_TARGET, params=params)
        print(request.text)
        if request.ok:
            return request.json()['ServiceResponse']['Courses']
        else:
            # TODO: Can we be more helpful?
            raise Exception('API request failed. Data returned: ' + request.text)

    def courses(self, subject: str, year: int = None, term: int = None) -> Course:
        """
        Generate a request to the API and fetch data on a desired set of courses.
        There are many options for how to identify a course through your parameters.
        :param subject: code of subject area for courses to search for. Example: ACCT, AFAM, PLSC, ENGL, EP&E, CPSC
        :param year: four-digit year of the term you're getting data on. API will use current year if not specified.abs
        :param term: term that course runs in. If not specified, the API will use the current default term (Spring or Fall).
                     This value changes to the next term on January 3rd and June 1st.
        """
        params = {
            'subjectCode': subject,
        }
        if year is not None:
            if term is None:
                raise Exception('A term must be specified with a year.')
            params['termCode'] = str(year) + str(term)
        return self.get(params)
