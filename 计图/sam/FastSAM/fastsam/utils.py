import torch

def adjust_bboxes_to_image_border(boxes, image_shape, threshold=20):
    '''Adjust bounding boxes to stick to image border if they are within a certain threshold.
    Args:
    boxes: (n, 4)
    image_shape: (height, width)
    threshold: pixel threshold
    Returns:
    adjusted_boxes: adjusted bounding boxes
    '''

    # Image dimensions
    h, w = image_shape

    # Adjust boxes
    boxes[:, 0] = torch.where(boxes[:, 0] < threshold, 0, boxes[:, 0])  # x1
    boxes[:, 1] = torch.where(boxes[:, 1] < threshold, 0, boxes[:, 1])  # y1
    boxes[:, 2] = torch.where(boxes[:, 2] > w - threshold, w, boxes[:, 2])  # x2
    boxes[:, 3] = torch.where(boxes[:, 3] > h - threshold, h, boxes[:, 3])  # y2

    return boxes



def bbox_iou(box1, boxes, iou_thres=0.9, image_shape=(640, 640), raw_output=False):
    '''Compute the Intersection-Over-Union of a bounding box with respect to an array of other bounding boxes.
    Args:
    box1: (4, )
    boxes: (n, 4)
    Returns:
    high_iou_indices: Indices of boxes with IoU > thres
    '''
    boxes = adjust_bboxes_to_image_border(boxes, image_shape)
    # obtain coordinates for intersections
    x1 = torch.max(box1[0], boxes[:, 0])
    y1 = torch.max(box1[1], boxes[:, 1])
    x2 = torch.min(box1[2], boxes[:, 2])
    y2 = torch.min(box1[3], boxes[:, 3])

    # compute the area of intersection
    intersection = (x2 - x1).clamp(0) * (y2 - y1).clamp(0)

    # compute the area of both individual boxes
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])

    # compute the area of union
    union = box1_area + box2_area - intersection

    # compute the IoU
    iou = intersection / union  # Should be shape (n, )
    if raw_output:
        if iou.numel() == 0:
            return 0
        return iou

    # get indices of boxes with IoU > thres
    high_iou_indices = torch.nonzero(iou > iou_thres).flatten()

    return high_iou_indices