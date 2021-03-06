Frequently Asked Questions
==========================

.. contents::

What is |appname|?
------------------

.. only:: edition_se

    dupeGuru is a tool to find duplicate files on your computer. It can scan either filenames or
    content. The filename scan features a fuzzy matching algorithm that can find duplicate
    filenames even when they are not exactly the same.

.. only:: edition_me

    dupeGuru Music Edition is a tool to find duplicate songs in your music collection. It can
    base its scan on filenames, tags or content. The filename and tag scans feature a fuzzy
    matching algorithm that can find duplicate filenames or tags even when they are not exactly
    the same.

.. only:: edition_pe

    dupeGuru Picture Edition (PE for short) is a tool to find duplicate pictures on your
    computer. Not only can it find exact matches, but it can also find duplicates among pictures
    of different kind (PNG, JPG, GIF etc..) and quality.

What makes it better than other duplicate scanners?
---------------------------------------------------

The scanning engine is extremely flexible. You can tweak it to really get the kind of results you
want. You can read more about dupeGuru tweaking option at the :doc:`Preferences page <preferences>`.

How safe is it to use dupeGuru?
-------------------------------

Very safe. dupeGuru has been designed to make sure you don't delete files you didn't mean to delete.
First, there is the reference folder system that lets you define folders where you absolutely
**don't** want dupeGuru to let you delete files there, and then there is the group reference system
that makes sure that you will **always** keep at least one member of the duplicate group.

What are the demo limitations of dupeGuru?
------------------------------------------

In demo mode, you can only perform actions on 10 duplicates at once. In 
`Fairware <http://open.hardcoded.net/about/>`_ mode, however, there are no limitations.

The mark box of a file I want to delete is disabled. What must I do?
--------------------------------------------------------------------

You cannot mark the reference (The first file) of a duplicate group. However, what you can do is to
promote a duplicate file to reference. Thus, if a file you want to mark is reference, select a
duplicate file in the group that you want to promote to reference, and click on
**Actions-->Make Selected into Reference**. If the reference file is from a reference folder
(filename written in blue letters), you cannot remove it from the reference position.

I have a folder from which I really don't want to delete files.
---------------------------------------------------------------

If you want to be sure that dupeGuru will never delete file from a particular folder, make sure to
set its state to **Reference** at :doc:`folders`.

What is this '(X discarded)' notice in the status bar?
------------------------------------------------------

In some cases, some matches are not included in the final results for security reasons. Let me use
an example. We have 3 file: A, B and C. We scan them using a low filter hardness. The scanner
determines that A matches with B, A matches with C, but B does **not** match with C. Here, dupeGuru
has kind of a problem. It cannot create a duplicate group with A, B and C in it because not all
files in the group would match together. It could create 2 groups: one A-B group and then one A-C
group, but it will not, for security reasons. Lets think about it: If B doesn't match with C, it
probably means that either B, C or both are not actually duplicates. If there would be 2 groups (A-B
and A-C), you would end up delete both B and C. And if one of them is not a duplicate, that is
really not what you want to do, right? So what dupeGuru does in a case like this is to discard the
A-C match (and adds a notice in the status bar). Thus, if you delete B and re-run a scan, you will
have a A-C match in your next results.

I want to mark all files from a specific folder. What can I do?
---------------------------------------------------------------

Enable the :doc:`Dupes Only <results>` mode and click on the Folder column to sort your duplicates
by folder. It will then be easy for you to select all duplicates from the same folder, and then
press Space to mark all selected duplicates.

.. only:: edition_se or edition_pe

    I want to remove all files that are more than 300 KB away from their reference file. What can I do?
    ---------------------------------------------------------------------------------------------------

    * Enable the :doc:`Dupes Only <results>` mode.
    * Enable the **Delta Values** mode.
    * Click on the "Size" column to sort the results by size.
    * Select all duplicates below -300.
    * Click on **Remove Selected from Results**.
    * Select all duplicates over 300.
    * Click on **Remove Selected from Results**.

    I want to make my latest modified files reference files. What can I do?
    -----------------------------------------------------------------------

    * Enable the :doc:`Dupes Only <results>` mode.
    * Enable the **Delta Values** mode.
    * Click on the "Modification" column to sort the results by modification date.
    * Click on the "Modification" column again to reverse the sort order.
    * Select all duplicates over 0.
    * Click on **Make Selected into Reference**.

    I want to mark all duplicates containing the word "copy". How do I do that?
    ---------------------------------------------------------------------------

    * Type "copy" in the "Filter" field in the top-right corner of the result window.
    * Click on **Mark --> Mark All**.

.. only:: edition_me
    
    I want to remove all songs that are more than 3 seconds away from their reference file. What can I do?
    ------------------------------------------------------------------------------------------------------

    * Enable the :doc:`Dupes Only <results>` mode.
    * Enable the **Delta Values** mode.
    * Click on the "Time" column to sort the results by time.
    * Select all duplicates below -00:03.
    * Click on **Remove Selected from Results**.
    * Select all duplicates over 00:03.
    * Click on **Remove Selected from Results**.

    I want to make my highest bitrate songs reference files. What can I do?
    -----------------------------------------------------------------------
    
    * Enable the :doc:`Dupes Only <results>` mode.
    * Enable the **Delta Values** mode.
    * Click on the "Bitrate" column to sort the results by bitrate.
    * Click on the "Bitrate" column again to reverse the sort order.
    * Select all duplicates over 0.
    * Click on **Make Selected into Reference**.

    I don't want [live] and [remix] versions of my songs counted as duplicates. How do I do that?
    ---------------------------------------------------------------------------------------------
    
    If your comparison threshold is low enough, you will probably end up with live and remix
    versions of your songs in your results. There's nothing you can do to prevent that, but there's
    something you can do to easily remove them from your results after the scan: post-scan
    filtering. If, for example, you want to remove every song with anything inside square brackets
    []:

    * Type "[*]" in the "Filter" field in the top-right corner of the result window.
    * Click on **Mark --> Mark All**.
    * Click on **Actions --> Remove Selected from Results**.    

I've tried to send my duplicates to Trash, but dupeGuru is telling me it can't do it. Why? What can I do?
---------------------------------------------------------------------------------------------------------

Most of the time, the reason why dupeGuru can't send files to Trash is because of file permissions.
You need *write* permissions on files you want to send to Trash. If you're not familiar with the
command line, you can use utilities such as `BatChmod`_ to fix your permissions.

If dupeGuru still gives you troubles after fixing your permissions, try enabling the "Directly
delete files" option that is offered to you when you activate Send to Trash. This will not send
files to the Trash, but delete them immediately. In some cases, for example on network storage
(NAS), this has been known to work when normal deletion didn't.

.. only:: edition_pe

    If you're trying to delete *iPhoto* pictures, then the reason for the failure is different. The
    deletion fails because dupeGuru can't communicate with iPhoto. Be aware that for the deletion
    to work correctly, you're not supposed to play around iPhoto while dupeGuru is working. Also,
    sometimes, the Applescript system doesn't seem to know where to find iPhoto to launch it. It
    might help in these cases to launch iPhoto *before* you send your duplicates to Trash.

If all of this fail, `contact HS support`_, we'll figure it out.

Where are user files located?
-----------------------------

For some reason, you'd like to remove or edit dupeGuru's user files (debug logs, caches, etc.).
Where they're located depends on your platform:

* Linux: ``~/.local/share/data/Hardcoded Software/dupeGuru``
* Mac OS X: ``~/Library/Application Support/dupeGuru``
* Windows: ``\Users\<username>\AppData\Local\Hardcoded Software\dupeGuru``

Preferences are stored elsewhere:

* Linux: ``~/.config/Hardcoded Software/dupeGuru.conf``
* Mac OS X: In the built-in ``defaults`` system, as ``com.hardcoded-software.dupeguru``
* Windows: In the registry, as ``HKEY_CURRENT_USER\Software\Hardcoded Software\dupeGuru``

For Music Edition and Picture Edition, replace "dupeGuru" by "dupeGuru Music Edition" and
"dupeGuru Picture Edition".

.. _BatChmod: http://www.lagentesoft.com/batchmod/index.html
.. _contact HS support: http://www.hardcoded.net/support
