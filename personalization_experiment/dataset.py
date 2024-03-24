def create(folder_path):
    '''
        faq:
            what are the required names of the 3 internal folders?
                - learner, nationality, proficiency
        input:
            - data folder with 3 internal folders:
                - learner own writings
                - learner same nationality writings
                - learner same proficiency writings
        output:
            - data folder with a train/test split of the learner own writings processed for training
            - the other folders processed for traiining
        example:
            python3 -m personal-learner dataset create ./my-folder
    '''
    print('creating dataset with folder :', folder_path)
