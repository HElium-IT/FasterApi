#!/bin/bash

ALIAS=fastapicli

sed -i "/alias $ALIAS/d" ~/.bashrc

source ~/.bashrc

echo "Alias $ALIAS removed"