# INFO : Path to the exoplanet CSV dataset
EXOPLANET_DATASET: str = 'exoplanet_dataset/PS_2024.01.30_14.51.36.csv'

# INFO: Descriptions of the columns in the exoplanet dataset


class descriptions:
    PL_NAME = 'Name of the planet'
    HOSTNAME = 'Name of the host star'
    PL_LETTER = 'Letter assigned to the planet'
    HD_ID = 'Unique identifier for the host star'
    HIP_ID = 'Hipparcos identifier for the host star including their positions and parallaxes'
    GAIA_ID = 'Unique identifier for celestial objects in the Gaia database'
    DEFAULT_FLAG = 'Default flag'
    SY_SNUM = 'Number of stars in the system of the planet'
    SY_PNUM = 'Number of planets in the system of the planet'
    SY_MNUM = 'Number of moons in the system of the planet'
    CB_FLAG = 'Indicates if the planet orbits two stars or just one'
    DISCOVERYMETHOD = 'Method used to discover the planet'
    DISC_YEAR = 'Year the planet was discovered'
    DISC_REFNAME = 'Reference to paper or publication where the discovery was reported'
    DISC_PUBDATE = 'Publication date of the discovery'
    DISC_LOCALE = 'Where the discovery was made'
    DISC_FACILITY = 'Facility where the discovery was made'
    DISC_TELESCOPE = 'Telescope used to discover the planet'
    DISC_INSTRUMENT = 'Instrument used to discover the planet'
    RV_FLAG = 'Indicates if the planet was discovered using the radial velocity method'
    PUL_FLAG = 'Indicates if the planet was discovered using the pulsar timing method'
    PTV_FLAG = 'Indicates if the planet was discovered using the pulsation timing variation method'
    TRAN_FLAG = 'Indicates if the planet was discovered using the transits method'
    AST_FLAG = 'Indicates if the planet was discovered using the astrometric variations method'
    OBM_FLAG = 'Indicates if the planet was discovered using the orbital brightness modulation method'
    MICRO_FLAG = 'Indicates if the planet was discovered using the microlensing method'
    ETV_FLAG = 'Indicates if the planet was discovered using the eclipse timing variations method'
    IMA_FLAG = 'Indicates if the planet was discovered using the imaging method'
    DKIN_FLAG = 'Indicates if the planet was discovered using the disk kinematics method'

    @staticmethod
    def get_all_descriptions() -> dict[str, str]:
        return {key: value for key, value in descriptions.__dict__.items() if not key.startswith('__')}
