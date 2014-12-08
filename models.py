from sqlalchemy import create_engine, Column, Integer, String
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

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
