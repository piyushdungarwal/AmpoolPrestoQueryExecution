#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
import warnings


def execute_query(
    url,
    payload,
    headers,
    prepare=False,
    ):
    cwd = os.getcwd()

    print '=============================================='
    print 'Query: ' + payload
    print '=============================================='

    response = requests.request('POST', url, headers=headers,
                                data=payload, verify=False)
    datajson = response.json()
    nextURL = datajson.get('nextUri')

    prepareHeader = ''
    result = []
    while nextURL is not None:
        resp = requests.request('GET', nextURL, headers=headers,
                                verify=False)

        if prepare == True and 'X-Presto-Added-Prepare' \
            in resp.headers.keys():
            prepareHeader = resp.headers['X-Presto-Added-Prepare']

    # print resp

        resp = resp.json()
        nextURL = resp.get('nextUri')

        if resp.get('stats').get('state') != 'FAILED':
            datalist = resp.get('data')
            if datalist is not None:
                result.extend(datalist)

    if prepare == True:
        return prepareHeader

    return result


def test_presto():
    warnings.filterwarnings('ignore')

    # Update AE master node ip here.
    url = 'https://10.1.4.109:9295/v1/statement'

    # 'YWRtaW46YWRtaW4=' is base64 encoded value of Presto username:Presto password. admin:admin in this case. Please update.
    authHeaders = {'Authorization': 'Basic YWRtaW46YWRtaW4='}

    query1 = \
        'prepare abc from select * from snowflake_tpch.public.region where r_regionkey < ?'
    headers1 = {'Content-Type': 'text/plain',
                'X-Presto-User': 'ampool',
                'X-Presto-Session': 'query_scancaching_enabled=false'}
    headers1.update(authHeaders)

    # Store prepare statement header, so that it can be used while actually executing queries.
    prepareHeader = execute_query(url, query1, headers1, True)
    print 'Prepare statement header:' + prepareHeader


    query2 = 'Execute abc using 3'

    # Please provide 'X-Presto-Prepared-Statement':<Prepare statement header> in headers for executing a prepared statement.
    headers2 = {
        'Content-Type': 'text/plain',
        'X-Presto-User': 'ampool',
        'X-Presto-Session': 'query_scancaching_enabled=false',
        'X-Presto-Prepared-Statement': prepareHeader,
        }
    headers2.update(authHeaders)
    result = execute_query(url, query2, headers2)
    print result
    print '(' + str(len(result)) + ' rows in result)'

    query3 = 'select * from snowflake_tpcds.public.call_center'
    headers3 = {'Content-Type': 'text/plain',
                'X-Presto-User': 'ampool',
                'X-Presto-Session': 'query_scancaching_enabled=false,enable_dynamic_filtering=true,join_distribution_type=BROADCAST'}
    headers3.update(authHeaders)
    result = execute_query(url, query3, headers3)
    print result
    print '(' + str(len(result)) + ' rows in result)'


test_presto()

