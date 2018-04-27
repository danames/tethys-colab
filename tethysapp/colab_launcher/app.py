from tethys_sdk.base import TethysAppBase, url_map_maker


class ColabLauncher(TethysAppBase):
    """
    Tethys app class for Google Collaboratory Launcher.
    """

    name = 'Google Colaboratory Launcher'
    index = 'colab_launcher:home'
    icon = 'colab_launcher/images/colab.png'
    package = 'colab_launcher'
    root_url = 'colab-launcher'
    color = '#3cba54'
    description = 'Launches the Google Colaboratory with a  Jupyter Notebook from HydroShare.'
    tags = 'HydroShare, Google, Python Notebooks, JupyterNotebooks'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='colab-launcher',
                controller='colab_launcher.controllers.home'
            ),
            UrlMap(
                name='loadresource',
                url='loadresource',
                controller='colab_launcher.controllers.loadresource'
            ),
        )

        return url_maps
