"""
Configuration

Author: Tong
Time: 24-06-2021
"""
user_id = "JingqiKang"  # github id
author_info = "Jingqi Kang"  # used in introduction
personal_link = "https://#####"  # used in introduction
repo_name = "multi-modal-event-extraction"  # repository name
branch_name = "main"  # branch name
your_research_topic = "MMEE"  # used for dictionary name
your_research_topic_full_name = "multi-modal event extraction"  # used for title
bib_link_overleaf = "https://www.overleaf.com/read/rgscdxhxbwhp"  # used for overleaf
color = "blue"

base_link = f"https://github.com/{user_id}/{repo_name}/{branch_name}/"

# user customized taxonomy
fined_taxonomy = {
    "Conference": ["ACL", "EMNLP", "NAACL", "COLING", "EACL", "CoNLL", "ICML", "ICLR", "NeurIPS", "AISTATS", "AAAI",
                   "IJCAI", "WWW", "MM", "CVPR", "ICCV", "ECCV", "WACV"],
    
    "Journal": [
        ["TACL", "Transactions of the Association for Computational Linguistics", "Trans. Assoc. Comput. Linguistics"],
        ["TKDE", "IEEE Transactions on Knowledge and Data Engineering", "{IEEE} Trans. Knowl. Data Eng."],
        ["TNNLS", "IEEE Transactions on Neural Networks and Learning Systems",
         "{IEEE} Trans. Neural Networks Learn. Syst."],
        ["IPM", "Information Processing and Managemen", "Inf. Process. Manag."],
        ["KBS", "Knowledge-BasedSystems", "Knowl. Based Syst."]],
    
    "Preprint": ["arXiv", "CoRR"],
    
    # 1: resource type
    "Contribution": ["Survey", "Important", "New Settings or Metrics", "New Application",
             "Empirical Study", "Theory", "New Backbone Model", "New Method", "Thesis", "Library", "Workshop",
             "Other Type"],
    # 2: Area
    "Area": ["CV", "NLP", "Multi-Modal", "Robotics"],
    
    # 3: Supervision
    "Supervision": ["Supervised Learning",
                    "Other Learning Paradigm"],
    
    # 4: Application
    "Application": ["Relation Extraction", "Event Extraction",
                    "Other Application", ],
    
    # 5: Approach
    "Approach": ["Rehearsal", "Meta-learning", "Other Approach"],
    
    # 6: Whether need memory
    "Memory": ["w/ External Knowledge", "w/o External Knowledge"],
    
    # 7: Setting
    "Setting": ["Class Incremental", "N-way K-shot", "Other Setting"],
    
    # 8: Research Question
    "RQs": {"Catastrophic Forgetting", "Order Sensitivity", "Few-shot Adaptation", "Others RQs"},
    
    # 9: Backbone
    "Backbone": ["BERTs", "Transformers", "Adapter", "RNNs", "CNNs", "GNNs", "Attentions", "Capsule Net",
                 "Probabilistic Graphical Model", "VAEs", "Other Structure"],
    
    # 10: Dataset
    "Dataset": ["Fewrel", "SimpleQuestion", "Tacred",
                "FewEvent",
                "Other Dataset"
                ],
    
    # 11: Metrics
    "Metrics": ["Accuracy", "F1"]
}