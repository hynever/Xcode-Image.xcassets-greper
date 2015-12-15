# coding=utf-8
import os
import shutil

imagePathArray = []

def copyImagesIntoTempDirectory():
    '''
            拷贝所有图片到临时目录
    '''

    tempDirName = 'ImageOptim'
    currentPwd = os.getcwd()
    tempDirPath = currentPwd+os.sep+tempDirName

    #创建ImageOptim目录
    os.mkdir(tempDirPath)
    
    #先获取所有的照片的路径
    fileNameArray = os.listdir(currentPwd)
    for fileName in fileNameArray:
        filePath = currentPwd + os.sep + fileName
        #如果fileName是目录，就在tempDirName中创建一个对应名称的目录
        dirName = tempDirPath + os.sep + fileName
        if os.path.isdir(filePath) and not os.path.exists(dirName) and fileName != tempDirName:
            os.mkdir(dirName)
        addImagePathToArrayWithDirPath(filePath)


    for imagePath in imagePathArray:
        #先删掉所有图片路径中的当前路径
        shortImagePath = imagePath.replace(currentPwd,'')
        shortImagePath = shortImagePath[1:]
        componentArray = shortImagePath.split('/')
        subDirName = componentArray[0]
        subDirPath = tempDirPath + os.sep + subDirName
        imageName = componentArray[-1]
        shutil.copyfile(imagePath,subDirPath + os.sep + imageName)


def addImagePathToArrayWithDirPath(dirPath):
    '''
        根据给定的路径获取这个目录及其子目录的所有图片
    '''

    if os.path.isfile(dirPath):
        extTuple = os.path.splitext(dirPath)
        if extTuple[1] == '.png':
            #加到数组中去
            imagePathArray.append(dirPath)
        else:
            return
    else:
        fileNameArray = os.listdir(dirPath)
        for fileName in fileNameArray:
            filePath = dirPath + os.sep + fileName
            addImagePathToArrayWithDirPath(filePath)



copyImagesIntoTempDirectory()
# string = "/User/Hello/World/"
# print string.split('/')