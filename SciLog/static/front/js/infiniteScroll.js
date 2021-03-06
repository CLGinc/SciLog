// Scroll globals
var pageNum = parseInt($('#items_list').attr('data-currentpage')), // current page
    hasNextPage = true, // Indicates whether to expect another page after this one
    viewParam = window.location.origin+window.location.pathname,
    datamode = $('#items_list').attr('data-mode'),
    datalastpage = 1,
    win = $(window),
    loadmorebtn = $("#loadmorebtn");
win.load(function(){
  datalastpage = $('#items_list').attr('data-pages');
  bindevent();
});
var bindevent = function(){
  if(datamode == 'infinitescroll'){
    win.on('scroll', loadOnScroll);
  } else if(datamode == 'loadmore') {
    $(loadmorebtn).bind('click', loadOnClick);
  }
};
var unbindevent = function() {
  if(datamode == 'loadmore'){
    $(loadmorebtn).unbind();
  } else if (datamode == 'infinitescroll') {
    $(win).unbind();
  }
};

// loadOnScroll handler
var loadOnScroll = function(event) {
   // If the current scroll position is past out cutoff point...
  var element = event.target;
  if(win.scrollTop() + win.height() == $(document).height()) {
  // temporarily unhook the scroll event watcher so we don't call a bunch of times in a row
  unbindevent();
  // execute the load function below that will visit the JSON feed and stuff data into the HTML
  loadItems();
  }
};
// loadOnClick handler
var loadOnClick = function(){
    // temporarily unhook the click event watcher so we don't call a bunch of times in a row
    unbindevent();
    // execute the load function below that will visit the JSON feed and stuff data into the HTML
    loadItems();
};
var loadItems = function() {
    $('#loading').addClass('is-active');
    // If the next page doesn't exist, just quit now
    if (hasNextPage === false) {
        $('#loading').removeClass('is-active');
        return false;
    }
    if (pageNum == datalastpage) {
      hasNextPage = false;
      $('#loading').removeClass('is-active');
      return false;
    }
    // Update the page number
    pageNum = ++pageNum;
    // Configure the url we're about to hit
    $.ajax({
        url: viewParam,
        data: {page: pageNum},
        type: "GET",
        dataType: 'html',
        success: function(data) {
            // Update global next page variable
            hasNextPage = true;//.hasNext;
    				$('#items_list').append(data);
            window.mdc.autoInit(document.getElementById('items_list'), () => {});
        },
        error: function(data) {
            // When I get a 400 back, fail safely
            hasNextPage = false;
        },
        complete: function(data){
            // Turn the scroll monitor back on
            bindevent();
            $('#loading').removeClass('is-active');
        }
    });
};
