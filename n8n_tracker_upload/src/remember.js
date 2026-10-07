// Remember Version — store the processed file's version so an unchanged file is skipped next time.
// n8n keeps this only for scheduled (published) runs, not manual test runs.
const memory = $getWorkflowStaticData('global');
memory.lastETag = $('Pick Tracker File').first().json.eTag;
return $input.all();
