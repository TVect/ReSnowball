- generate_tuple:

从 NER tag 的句子中选择出 entity1 & entity2 为指定类型的句子，构造 tuple. 作为 processed_tuple

- init_bootstrapp

while loop:

    1. 从所有 processed_tuple 中匹配出和 seed tuple 匹配的 matched_tuple (对 entity 的名字做匹配)

    2. 对 matched_tuple 做聚类, 构造出 self.patterns, 记录下每个 pattern 下对应的 tuple 个数
    
        按 min_pattern_support 做一次过滤
    
    for each tuple in processed_tuple:

        for each pattern in self.patterns:
        
            计算 tuple 和 pattern 之间的相似性，是否大于 threshold_similarity
        
            如果大于：更新 pattern 的 selectivity，将 tuple 的 entity1&entity2 和 seed_tuples 做比较，看是否冲突
                        更新 positive / negative / unknown 的统计数据
        
        记录下和该 tuple 的最相似的 pattern（后续用来计算 tuple 的置信度）, 如果相似度大于 threshold_similarity
    
    计算更新每个 pattern 的置信度
    计算每个 tuple 的置信度
    
    过滤出置信度大于 instance_confidance 的tuple，加到 seed tuple 中

