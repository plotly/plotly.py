import pandas as pd

def preprocess_sunburst_treemap(df, path, value_column, other_columns=None):
    df_all_trees = pd.DataFrame(columns=['labels', 'parent', 'id'])
    if isinstance(path, list):
        for i, level in enumerate(path):
            df_tree = pd.DataFrame(columns=['labels', 'parent', 'id'])
            dfg = df.groupby(path[i:]).sum(numerical_only=True)
            dfg = dfg.reset_index()
            df_tree['labels'] = dfg[level].copy().astype(str)
            df_tree['parent'] = ''
            df_tree['id'] = dfg[level].copy().astype(str)
            if i < len(path) - 1:
                j = i + 1
                while j < len(path):
                    df_tree['parent'] += dfg[path[j]].copy().astype(str)
                    df_tree['id'] +=  dfg[path[j]].copy().astype(str)
                    j += 1
            else:
                df_tree['parent'] = 'total'

            if i == 0 and other_columns:
                df_tree[other_columns] = dfg[other_columns]
            elif other_columns:
                for col in other_columns:
                    df_tree[col] = ''
            df_tree[value_column] = dfg[value_column]
            #df_tree[color_column] = dfg[color_column]
            df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series({'labels': 'total', 'id': 'total', 'parent': '',
                        value_column:df[value_column].sum(),
                        #color_column:df[color_column].sum(),
                        })
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees
