import math
import cmath

def CstResultParameters(mws, *, parent_path=r'1D Results\S-Parameters', run_id=0, result_id=0):
    result_tree = mws.Resulttree

    result_path_list = list()
    if result_tree.DoesTreeItemExist(parent_path):
        child = result_tree.GetFirstChildName(parent_path)

        while len(child) > 0:
            result_path_list.append(child)
            child = result_tree.GetNextItemName(child)

        run_ids = result_tree.GetResultIDsFromTreeItem(result_path_list[result_id])
        run_id_name = list(run_ids)[run_id]
        object_res = result_tree.GetResultFromTreeItem(result_path_list[result_id], run_id_name)
        result_type = object_res.GetResultObjectType

        frequencies_list = list(object_res.GetArray('x'))

        if result_type == '1DC':
            y_real = list(object_res.GetArray('yre'))
            y_imag = list(object_res.GetArray('yim'))

            y_list = []
            for i, yval in enumerate(y_real):
                y_list.append(20 * math.log10(abs(complex(y_real[i], y_imag[i]))))
        else:
            y_list = list(object_res.GetArray('y'))

        x_label = object_res.GetXLabel
        y_label = object_res.GetYLabel
        plot_title = object_res.GetTitle

        if result_type == '1DC':
            return frequencies_list, [y_real, y_imag], y_list, [x_label, y_label, plot_title]
        else:
            return frequencies_list, y_list, [x_label, y_label, plot_title]
    else:
        print('Result tree item not found.')
