// Draw Mermaid fences, and draw them again when the palette toggle changes.
// A fence that includes its own theme config keeps that config.
(function () {
  var rendering = false;
  var queued = false;
  var scheme = null;

  function currentScheme() {
    return document.body.getAttribute("data-md-color-scheme") || "default";
  }

  function stash(node) {
    if (!node.dataset.agentsphereSource) {
      node.dataset.agentsphereSource = node.textContent.replace(/^\n+|\n+$/g, "");
    }
  }

  function render() {
    if (!window.mermaid) {
      return;
    }
    if (rendering) {
      queued = true;
      return;
    }
    var nodes = document.querySelectorAll(".mermaid");
    if (!nodes.length) {
      return;
    }
    rendering = true;
    var dark = currentScheme() === "slate";
    nodes.forEach(function (node) {
      stash(node);
      node.removeAttribute("data-processed");
      node.textContent = node.dataset.agentsphereSource;
    });
    window.mermaid.initialize({
      startOnLoad: false,
      securityLevel: "strict",
      theme: dark ? "dark" : "default",
    });
    Promise.resolve(window.mermaid.run({ querySelector: ".mermaid" })).then(
      function () {
        rendering = false;
        if (queued) {
          queued = false;
          render();
        }
      },
      function () {
        rendering = false;
        queued = false;
      }
    );
  }

  if (!window.__agentsphereMermaidWatch) {
    window.__agentsphereMermaidWatch = true;
    new MutationObserver(function () {
      var next = currentScheme();
      if (next === scheme) {
        return;
      }
      scheme = next;
      render();
    }).observe(document.body, {
      attributes: true,
      attributeFilter: ["data-md-color-scheme"],
    });
  }

  function boot() {
    scheme = currentScheme();
    if (window.mermaid) {
      window.mermaid.initialize({ startOnLoad: false, securityLevel: "strict" });
    }
    render();
  }

  if (window.document$) {
    window.document$.subscribe(boot);
  } else {
    document.addEventListener("DOMContentLoaded", boot);
  }
})();
