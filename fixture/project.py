from model.project import Project


class ProjectHelper:

    def __init__(self,app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_data("name", project.name)
        self.change_field_data("description", project.description)

    def change_field_data(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count_projects(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr")[2:])

    project_cache = None

    def get_projects_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr")[2:]:
                name = element.find_element_by_xpath("./td[1]/a").text
                description = element.find_element_by_xpath("./td[5]").text
                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)

    def select_project_by_index(self, index):
        wd = self.app.wd
        selected_project = wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr")[2:][index]
        selected_project.find_element_by_xpath("./td[1]/a").click()

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_index(index)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cache = None