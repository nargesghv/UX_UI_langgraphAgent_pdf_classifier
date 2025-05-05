import React from 'react';
import { Document, Page } from 'react-pdf';

function Preview({ file }) {
  return (
    <div className="mt-6">
      {file && file.type === "application/pdf" ? (
        <Document file={file}>
          <Page pageNumber={1} />
        </Document>
      ) : (
        <p className="text-sm text-gray-600">Preview not available for this file type.</p>
      )}
    </div>
  );
}

export default Preview;
