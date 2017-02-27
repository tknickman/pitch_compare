
// force dc.js to be responsive
$( window ).resize(function() {
    dc.renderAll();
});

// charts loading overlay
$(".main-panel").LoadingOverlay("show");
