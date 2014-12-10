import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.sqlite')
Base = declarative_base()


class Organization(Base):
    """
    Organization

    Description

    Attributes:
        id: An auto-incrementing numerical identifier.
        name: The name of the organization.
        oui: The MA-L/OUI assigned to the organization.
        address: The address of the organization.
    """
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    oui = Column(Integer)
    address = Column(String)

    def to_dictionary(self):
        """
        Convert an oranization to a dictionary.

        Args:
            self

        Returns:
            A dictionary with the organization's name, OUI, and address.
        """
        return {'name': self.name, 'oui': self.oui, 'address': self.address}


class MetaData(Base):
    """
    MetaData

    Description

    Attributes:
        hash: The SHA-1 hash of the MA-L/OUI listing at the time it was updated.
        generated: The date (UTC) the MA-L/OUI listing was generated.
        updated: The date (UTC) the MA-L/OUI listing was entered into the DB.
    """
    __tablename__ = 'metadata'
    id = Column(Integer, primary_key=True)
    hash = Column(String)
    generated = Column(DateTime, nullable=False)
    updated = Column(
        DateTime, default=datetime.datetime.utcnow, nullable=False
    )

    def to_dictionary(self):
        """
        Convert MetaData entry to a dictionary.

        Args:
            self

        Returns:
            A dictionary with the entry's hash, generated time and updated time.
        """
        return {'hash': self.hash, 'generated': self.generated,
                'updated': self.updated}

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
