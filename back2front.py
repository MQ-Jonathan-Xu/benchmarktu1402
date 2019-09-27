import numpy as np


def convert(job):

    """
    Convert backend job to frontend job.

    Parameters
    ----------
    job: gui.Job
        The frontend job instance.

    Returns
    -------
    job: Job
        The backend job instance.
    """

    pass


class Job:

    def __init__(self, name):
        # Specify default job name
        self.setName(name)

        # Specify default model value
        self.setModel(0)

        # Specify default thickness and damage value
        self.setThickness(0.1)
        self.setDamage(0.1)

        # Set default values for material properties
        self.setMaterial(np.array([[1.8e11, 0.3, 10]]))

        # Set default values for boundary conditions
        self.setBoundaries(np.array([[1e15, 1e11, 20]]))

        # Set default values for corrosion wastage
        self.setCorrosion(np.array([[0.0, 0.5]]))

        # Set default values for environmental temperature
        self.setTemperature(np.array([[10, 0.5]]))

        # Set default type of analysis
        self.setAnalysis('Modal')

        # Set default values for modal analysis
        self.setModalSettings(5, 'Mass')

        # Set default values for time history analysis
        self.setTimeHistorySettings(0.005, 0.005, 10, 0.1, 0)


    def setName(self, name):

        """
        Specify the name of the job.

        Parameters
        ----------
        name: str
            The name of the job.
        """

        self._name = name

    def getName(self):
        return self._name


    def setModel(self, model):

        """
        Specify the model to be analyzed.

        Parameters
        ----------
        model: {0, 1, 2, 3, 4, 5, 6}
            The model index corresponding to the following cases:
                0:  Healhty state
                1:  Damage state 1
                2:  Damage state 2
                3:  Damage state 3
                4:  Damage state 4
                5:  Damage state 5
                6:  Damage state 6
        """

        self._model = model

    def getModel(self):
        return self._model


    def setThickness(self, thickness):

        """
        Specify the model thickness.

        Parameters
        ----------
        thickness: float, positive
            The thickness of the model.
        """
        self._thickness = thickness

    def getThickness(self):
        return self._thickness


    def setDamage(self, damage):

        """
        Specify the degree of severity, i.e., stiffness reduction, at the
        damaged areas.

        Parameters
        ----------
        damage: float
            The percentage [0-1] of stiffness reduction at the damaged areas.
        """

        self._damage = damage

    def getDamage(self):
        return self._damage


    def setMaterial(self, material):

        """
        Specify the material properties and their dependency on temperature.

        Parameters
        ----------
        material: ndarray
            The 2-dimensional ndarray of shape n x 3 containing the 
            dependency of material properties on temperature, with n 
            representing the number of temperature values at which the 
            material properties are specified. The first two columns of the 
            array contain the values of elastic molulus and Poisson ratio and
            the second one stores the corresponding temperatures of each 
            property value. If only one temperature value is specified, the 
            material properties are temperature independent.
            
        Example
        -------
        job = Job('Job-1')
        material = np.array([
                [2.1e11, 0.3,  0],
                [1.9e11, 0.3, 20],
                [1.8e11, 0.1, 30]])
        job.setMaterial(material)
        """

        self._material = material

    def getMaterial(self):
        return self._material


    def setBoundaries(self, boundary1, boundary2=None, boundary3=None):

        """
        Specify the boundary conditions and their dependency on temperature.

        Parameters
        ----------
        boundary1: ndarray
            The 2-dimensional ndarray of shape n x 3 containing the dependency
            of boundary conditions at the left-most support point on 
            temperature, with n being the number of temperature values at 
            which the boundary stiffness is specified. The first two columns 
            of the array contain the values of stiffness in x and y directions
            and the second one stores the corresponding temperature values.
            If only one temperature value is specified, boundary conditions 
            are temperature independent.
        boundary2: ndarray, optional
            Similar to boundary1 but referring to the support point at the 
            middle of the system.
        boundary3: ndarray, optional
            Similar to boundary1 but referring to the rightmost support point.
        """

        self._boundary1 = boundary1
        self._boundary2 = boundary1 if boundary2 is None else boundary2
        self._boundary3 = boundary1 if boundary3 is None else boundary3

        return self._boundary1, self._boundary2, self._boundary3


    def getBoundaries(self):
        return self._boundary1, self._boundary2, self._boundary3


    def setCorrosion(self, corrosion):

        """
        Specify the distribution of corrosion wastage along the length of 
        the system.

        Parameters
        ----------
        corrosion: ndarray
            The 2-dimensional ndarray of shape n x 2 containing the 
            distribution of corrosion wastage, with n representing the number 
            of points in space at which the temperature is specified. The 
            first column of the array contains the values of corrosion wastage 
            and the second one stores the corresponding position (x / L) of 
            each corrosion value. A uniform profile is assumed when only a 
            single point in space is specified.
        """

        self._corrosion = corrosion

    def getCorrosion(self):
        return self._corrosion


    def setTemperature(self, temperature):

        """
        Specify the distribution of temperature along the length of the system.

        Parameters
        ----------
        temperature: ndarray
            The 2-dimensional ndarray of shape n x 2 containing the 
            distibution of temperature, with n representing the number of
            points in space at which the temperature is specified. The first 
            column of the array contains the temperature values and the second
            one stores the corresponding position (x / L) of each temperature
            value. A uniform profile is assumed when only a single point in 
            space is specified.
        """

        self._temperature = temperature

    def getTemperature(self):
        return self._temperature


    def setAnalysis(self, analysis):

        """
        Specify the type of analysis to be performed.

        Parameters
        ----------
        analysis: {'Modal', 'Time history'}
            The type of analysis to be executed.
        """

        self._analysis = analysis

    def getAnalysis(self):
        return self._analysis


    def setModalSettings(self, modes, normalization):
        
        """
        Specify the settings for modal analysis.

        Parameters
        ----------
        modes: int, positive
            The number of vibration modes to be extracted.
        normalization: {'Mass', 'Displacement'}
            The normalization method mode shapes.
        """

        self._modalSettings = {}
        self._modalSettings['Modes'] = modes
        self._modalSettings['Normalization'] = normalization

    def getModalSettings(self):
        return self._modalSettings


    def setTimeHistorySettings(self, alpha, beta, period, increment, lcase):
        
        """
        Specify the settings for time history analysis.

        Parameters
        ----------
        alpha: float, positive
            ...
        beta: float, positive
            ...
        period: float, positive
            ...
        increment: float, positive
            ...
        lcase: {0, 1, 2}
            ...
        """

        self._timeHistorySettings = {}
        self._timeHistorySettings['Alpha'] = alpha
        self._timeHistorySettings['Beta'] = beta
        self._timeHistorySettings['Period'] = period
        self._timeHistorySettings['Increment'] = increment
        self._timeHistorySettings['lcase'] = lcase

    def getTimeHistorySettings(self):
        return self._timeHistorySettings