from fastapi import APIRouter, status, Depends, Response
from .. import json_schemas
import pandas as pd
from pool_api.database import get_df

router = APIRouter(
    tags=['Pool'],
    prefix='/pool'
)


# POST
@router.post('/', status_code=status.HTTP_201_CREATED)
def insert_or_append(pool: json_schemas.Pool, response: Response, df: pd.DataFrame = Depends(get_df)):
    poolId = pool.poolId

    if pool.poolId in df.index:
        arr = df.loc[poolId][0].split(' ')
        for value in pool.poolValues:
            arr.append(str(value))

        arr_to_str = ' '.join(arr)
        df.loc[poolId] = arr_to_str
        df.to_csv('pool_api/data.csv')

        response.status_code = status.HTTP_202_ACCEPTED
        return 'appended'

    else:
        df.reset_index(inplace=True)
        pool_vals = [str(val) for val in pool.poolValues]
        pool_vals_str = ' '.join(pool_vals)
        pool_dict = {'poolId': poolId, 'poolValues': pool_vals_str}
        df = df.append(pool_dict, ignore_index=True)
        df.to_csv("pool_api/data.csv", index=False)

        return 'inserted'


@router.post('/{poolId}', status_code=status.HTTP_200_OK)
def quantile_query(poolId: int, percentile: int, df: pd.DataFrame = Depends(get_df)):
    str_ls = df.loc[poolId][0].split(' ')
    int_ls = [int(x) for x in str_ls]
    ls_len = len(int_ls)
    rank = percentile / 100 * (ls_len - 1) + 1

    if rank.is_integer():
        rank = int(rank)
        p_num = int_ls[rank]

    else:
        int_part, frac_part = divmod(rank, 1)
        int_part = int(int_part)
        p_num = int_part + rank * (int_ls[int_part+1] - int_ls[int_part])

    return {'calculated_quantile': p_num,
            'total_count': ls_len}
