import dropbox


class TransferData:
    def __init__(self, token):
        self.token = token

    def upload(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.token)

        f = open(file_from, 'rb'):
            dbx.files_upload(f.read(), file_to)

def main():
    token = '5vF4g1BGzmsAAAAAAAAAAa6tbBKbmS0VnQy4r-Y2Zg21IN9atTeV-KvFdFMQyAjK'
    transferData = TransferData(token)

    file_from = input('Enter source path: ')
    file_to = input('Enter end path: ')

    transferData.upload(file_from, file_to)
    print('Done')

main()