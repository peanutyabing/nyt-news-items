# New York Times News Items

## Squirro Delivery Challenge

script.py calls the New Yorks Times Article Search API and returns news items in batches.

Each batch is a list of flattened dictionaries.

To run the script, clone this repository, import necessary dependencies (refer to requirements.txt), and run this from the root of the directory:

```console
$ python3 script.py

```

Snapshot of output:

```console
0 Batch of 10 items
  - nyt://article/d476130a-57be-53c6-9efe-3bb61a42e8c7 - Silicon Valley, Cradle of Computer Chips, Gains Big New Research Center
  - nyt://article/e0f52b03-1131-51ef-9b03-19869fdd7a05 - Regulators Rebut Claims by Silicon Valley Bank’s Ex-C.E.O.
  - nyt://video/72709f83-a587-530b-a27d-0a4541831463 - Senators Grill Ex-C.E.O. of Silicon Valley Bank
  - nyt://article/55fdee84-0cbc-54f1-ac30-d47fc40304ca - ‘Do You Even Want Us to Exist?’ A Bank Chief Fights to Survive.
  - nyt://article/b5593cdb-0b4e-5904-a240-523a8a8b3d89 - Savoring a California Wine Country Far From Napa and the Crowds
  - nyt://article/7d2205b6-09cb-5986-80d6-7dffdf41cde6 - Silicon Valley Bank’s Ex-C.E.O. Is ‘Truly Sorry’ but Deflects Blame
  - nyt://article/a6ed8ce3-c7af-54d9-9649-bad2ae480fec - A Week With the Wild Children of the A.I. Boom
  - nyt://article/fb40663f-a9fe-5ede-a6a5-491154b59032 - Goldman Says U.S. Is Investigating Its Work for Silicon Valley Bank
  - nyt://article/ee48909c-7cfc-5954-9833-09df6343aeaf - Fed Officials Were Split Over June Rate Pause, Minutes Show
  - nyt://article/676c6476-f1d9-5926-bd30-25307731dbb6 - Reid Hoffman Is on a Mission: To Show A.I. Can Improve Humanity
1 Batch of 10 items
  - nyt://article/d126c17f-f91a-5f9a-929d-fd1e62fcfdb2 - Corporate America Faces a Bankruptcy Boom
  - nyt://article/249bb1cc-294e-53bd-a06c-d59e58070d26 - San Francisco Fed Ties to S.V.B. Chief Attracts Scrutiny to Century-Old Setup
  ...

```
