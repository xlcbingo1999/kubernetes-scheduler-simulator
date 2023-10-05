import yaml

# 读取原始的 YAML 文件
with open('/root/kubernetes-scheduler-simulator/data/openb_pod_list_micro/openb_node_list_gpu_node_full.yaml', 'r') as input_file:
    # 使用 safe_load_all 逐个加载 YAML 文档
    documents = yaml.safe_load_all(input_file)

    # 获取前 30 个项目
    first_30_items = []
    for i, doc in enumerate(documents):
        if i >= 50:
            break
        first_30_items.append(doc)

# 保存前 30 个项目为一个新的 YAML 文件
with open('/root/kubernetes-scheduler-simulator/data/openb_pod_list_micro/openb_node_list_gpu_node.yaml', 'w') as output_file:
    for index, item in enumerate(first_30_items):
        yaml.dump(item, output_file, default_flow_style=False)
        if index < len(first_30_items) - 1:
            output_file.write('\n---\n\n')  # 使用 "---" 分隔每个项目
