from utilities.configuration import Configuration
import pymongo


class BaseMongo:
    def __init__(self):
        self.client = pymongo.MongoClient(Configuration().connection_URL)
        self.db = self.client[Configuration().db_name]
        # self.collection_name = self.client[collection_name]

    def add_new_data(self, collection_name: str, document_data: dict | list):
        """
        :param collection_name: name of collection
        :param document_data: the data of new document(s), will add one document if document_data get dict
               or many documents if document_data get list of dicts
        :return:
        """
        if type(document_data) is dict:
            self.db[collection_name].insert_one(document_data)
        elif type(document_data) is list:
            self.db[collection_name].insert_many(document_data)

    def find_document(self, collection_name: str, search_options: dict = {}, out_put_options: dict = {}):
        """
        :param collection_name: name of collection
        :param search_options: optional argument
        :param out_put_options: optional argument
        :return: result of search dict
        """
        search_result = self.db[collection_name].find_one(search_options, out_put_options)
        return search_result

    def find_documents(self, collection_name: str, search_options: dict = {}, out_put_options: dict = {}):
        """
        :param collection_name: name of collection
        :param search_options: optional argument
        :param out_put_options: optional argument
        :return: result of search list of dicts
        """
        search_result = self.db[collection_name].find(search_options, out_put_options)
        return search_result

    def delete_document(self, collection_name: str, search_options: dict = {}):
        """
        :param collection_name: name of collection
        :param search_options: optional argument, if search_options get empty dict will delete the first document
        """
        self.db[collection_name].delete_one(search_options)

    def delete_documents(self, collection_name: str, search_options: dict = {}):
        """
        :param collection_name: name of collection
        :param search_options: optional argument, if search_options get empty dict will delete the all documents
        """
        self.db[collection_name].delete_many(search_options)

    def update_document(self, query: list, collection_name: str, search_options: dict = {}):
        """
        :param query: is mandatory argument, update options
        :param collection_name: the name of collection
        :param search_options: optional argument, if search_options get empty dict change will apply for
               first document.
        """
        self.db[collection_name].update_one(search_options, query)

    def update_documents(self, query: list, collection_name: str, search_options: dict = {}):
        """
        :param query: is mandatory argument, update options
        :param collection_name: the name of collection
        :param search_options: optional argument, if search_options get empty dict change will apply for
               all documents in collection
        """
        self.db[collection_name].update_many(search_options, query)

    def delete_collection(self, collection_name: str):
        self.db[collection_name].drop()
