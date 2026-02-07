
# DataCard

DataCard is the most effective way to move data around an organization,
and evolves from two highly-effective time-proven user interface designs.

 - Terminals
    - Pros: Fast. Honest (i.e. programs rarely lie about their data/errors to the user).
    - Cons: No graphics, sequential "one command at a time" processing. Limited extensibility around those two traits (see sixel, kitty). Ephemeral, does not store data being manipulated across app sessions.
 - Spreadsheets
    - Pros: Graphics. Parallel, "Compute X on all the numbers all the time" processing. Ability to see inputs and outputs at the same time, and "internal" working data. Some extensibility w/r/t macros and cell functions. Stores data across app sessions.
    - Cons: Limited quantities of data processable, leaky abstractions (e.g. difficult to do a dictionary lookup or re-use forumulas in a different spreadsheet)

This allows us to infer the properties of an ideal data processing system:

 - Fast
 - Honest
 - Graphics
 - Parallel "always compute Y from X for all X" data processing - NOT sequential
 - Persist data across sessions

```
+--------------------------------------------
|
|           Table view w/ 2 options:
|      Tabs of tables || Nodes of tables w/ links between
|                        them describing derived/calculated fields
|
|
|
|-------------------------------------------
|               Terminal; tabs? Tabs.
|
+-------------------------------------------
````

Whole window pop-ups:

 - Create new Table view
    - select a table from any database w/ offer to attempt creation of new one given schema (sqlite, postgres, sqlserver, mysql, mariadb)
 -


# Development Setup

Step 1: Install python.

Step 2: Have an internet connection.

Step 3:

```bash
python -m build
```





