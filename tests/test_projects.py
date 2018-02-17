import unittest
import os
exec(open(os.path.join(os.environ['NBI_PROJECTS_DIR'],
                       'projects-envvars.py')).read())
from projects.models import Project
from projects import app


class FairTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True

        # Required folders
        folders = {}
        folders['DATA_FOLDER'] = app.config['DATA_FOLDER'] = os.getcwd() + "/data"
        folders['UPLOAD_FOLDER'] = app.config['UPLOAD_FOLDER'] = os.getcwd() + "/images"
        # Create required folders for the application if they don't exist
        for key, folder in folders.items():
            try:
                os.makedirs(folder)
                print("Created: " + folder)
            except FileExistsError:
                pass

        app.config['WTF_CSRF_ENABLED'] = False
        # Override default DB setting -> use a testing db instead of the default
        app.config['DB'] = app.config['DATA_FOLDER'] + "/dataset_test"
        self.app = app.test_client()

    def tearDown(self):
        # Clean up
        Project.clear()
        self.assertTrue(len(Project.get_all()) == 0)

    def test_dummy(self):
        self.assertTrue(True)

    def create_user(self):
        pass

if __name__ == '__main__':
    unittest.main()
