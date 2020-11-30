# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:40:30 2020

@author: Anthony Chedid
"""


import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_connection2(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn,create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c=conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_test(conn,test):
    sql=''' INSERT INTO benchmarks(deviceName,Astar,AstarSpec,Duplicates,DuplicatesSpec,BubbleSort,BubbleSortSpec,InsertionSort,InsertionSortSpec,SelectionSort,SelectionSortSpec,QuickSort,QuickSortSpec,MergeSort,MergeSortSpec,HeapSort,HeapSortSpec,Huffman,HuffmanSpec,Queens,QueensSpec,geometricMean)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur=conn.cursor()
    cur.execute(sql,test)

    conn.commit()

    return cur.lastrowid

def insert(dic, AstarSpec, DuplicatesSpec, BubbleSortSpec, InsertionSortSpec, SelectionSortSpec, QuickSortSpec, MergeSortSpec, HeapSortSpec, HuffmanSpec, QueensSpec, geometricMean):
    conn=create_connection2(r"benchmarks.db")
    sql_create_benchmarks_table=""" CREATE TABLE IF NOT EXISTS benchmarks(
                                        id integer PRIMARY KEY,
                                        deviceName text NOT NULL,
                                        Astar double,
                                        AstarSpec double,
                                        Duplicates double,
                                        DuplicatesSpec double,
                                        BubbleSort double,
                                        BubbleSortSpec double,
                                        InsertionSort double,
                                        InsertionSortSpec double,
                                        SelectionSort double,
                                        SelectionSortSpec double,
                                        QuickSort double,
                                        QuickSortSpec double,
                                        MergeSort double,
                                        MergeSortSpec double,
                                        HeapSort double,
                                        HeapSortSpec double,
                                        Huffman double,
                                        HuffmanSpec double,
                                        Queens double,
                                        QueensSpec double,
                                        geometricMean double
                                        );"""


    if conn is not None:
        create_table(conn,sql_create_benchmarks_table)

    else:
        print("Error!")

    with conn:
        # create a new test
        project = (dic["NAME"], dic["Astar"], AstarSpec, dic["remove_duplicates"], DuplicatesSpec, dic["bubbleSort"],BubbleSortSpec,dic["insertionSort"],InsertionSortSpec,dic["selectionSort"],SelectionSortSpec,dic["quickSort"],QuickSortSpec,dic["merge"],MergeSortSpec,dic["heapSort"],HeapSortSpec,dic["huff"],HuffmanSpec,dic["queen"],QueensSpec,geometricMean);
        create_test(conn, project)
