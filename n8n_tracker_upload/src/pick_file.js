// Pass the uploaded files on to the next read step (that step reads only its own file; a missing file is skipped)
return [{ json: {}, binary: $('Upload Tracker').first().binary || {} }];
