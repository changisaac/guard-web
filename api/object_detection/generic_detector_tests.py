import os
from generic_detector import GenericDetector

def end_to_end_image(file_name):
    detector = GenericDetector()
    boxes = detector.get_bounding_boxes(file_name)

    test_ref = [[0, 'person', 0.999508261680603, [728, 1109, 698, 1649]],
               [0, 'person', 0.9971250295639038, [2291, 1016, 838, 1697]],
               [0, 'person', 0.996671199798584, [1836, 982, 663, 1732]],
               [0, 'person', 0.9948155879974365, [1349, 1136, 550, 1553]]]

    if boxes == test_ref:
        print('TEST SUCCESS')
        print(boxes)
    else:
        print(boxes)
        print('TEST FAIL')

def end_to_end_video(file_name):
    detector = GenericDetector()
    boxes = detector.get_bounding_boxes(file_name)

    print(boxes)

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    end_to_end_image(dir_path + '/test_data/end_to_end_image.jpg')
    #end_to_end_video(dir_path + '/test_data/end_to_end_video.avi')

if __name__ == '__main__':
    main()
