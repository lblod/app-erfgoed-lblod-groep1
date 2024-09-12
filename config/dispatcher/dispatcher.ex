
defmodule Dispatcher do
  use Matcher
  define_accept_types [
    html: ["text/html", "application/xhtml+html"],
    json: ["application/json", "application/vnd.api+json"],
    upload: ["multipart/form-data"],
    sparql_json: ["application/sparql-results+json"],
    any: [ "*/*" ],
  ]

  define_layers [ :api, :frontend, :not_found ]

  ###############################################################
  # files
  ###############################################################

  get "/files/:id/download", %{ accept: [:any], layer: :api } do
    Proxy.forward conn, [], "http://file/files/" <> id <> "/download"
  end

  post "/files/*path", %{ accept: [:json], layer: :api } do
    Proxy.forward conn, path, "http://file/files/"
  end

  match "/files/*path", %{ accept: [:json], layer: :api } do
    Proxy.forward conn, path, "http://cache/files/"
  end

  ###############################################################
  # login
  ###############################################################

  match "/sessions/*path", %{ accept: [:json], layer: :api} do
    Proxy.forward conn, path, "http://login/sessions/"
  end

  match "/accounts", %{ accept: [:json], layer: :api} do
    Proxy.forward conn, [], "http://cache/accounts/"
  end

  match "/accounts/*path", %{ accept: [:json], layer: :api} do
    Proxy.forward conn, path, "http://accountdetail/accounts/"
  end

  match "/groups/*path", %{ accept: [:json], layer: :api} do
    Proxy.forward conn, path, "http://cache/groups/"
  end

  match "/sites/*path", %{ accept: [:json], layer: :api} do
    Proxy.forward conn, path, "http://cache/sites/"
  end

  match "/permission-classification-codes/*path", %{ accept: [:json], layer: :api} do
    Proxy.forward conn, path, "http://cache/permission-classification-codes/"
  end
  

  match "/mock/sessions/*path", %{ accept: [:any], layer: :api} do
    Proxy.forward conn, path, "http://mock-login/sessions/"
  end

  ###############################################################
  # sparql endpoint
  ###############################################################

  post "/sparql/*path", %{ accept: [:sparql_json], layer: :api } do
    Proxy.forward conn, path, "http://database:8890/sparql/"
  end

  #################################################################
  # Address search
  #################################################################

  match "/adresses-register/*path" do
    forward conn, path, "http://adressenregister"
  end
  ###############################################################
  # frontend
  ###############################################################

  match "/assets/*path", %{ accept: [:any], layer: :api } do
    Proxy.forward conn, path, "http://frontend/assets/"
  end

  match "/@appuniversum/*path", %{ accept: [:any], layer: :api } do
    Proxy.forward conn, path, "http://frontend/@appuniversum/"
  end

  match "/bestuurseenheid-classificatie-codes/*path", %{layer: :api, accept: %{json: true}} do
    forward(conn, path, "http://cache/bestuurseenheid-classificatie-codes/")
  end

  match "/bestuurseenheid/*path", %{layer: :api, accept: %{json: true}} do
    forward(conn, path, "http://cache/bestuurseenheid/")
  end

  match "/locatie/*path", %{layer: :api, accept: %{json: true}} do
    forward(conn, path, "http://cache/locatie/")
  end

  match "/adres/*path", %{layer: :api, accept: %{json: true}} do
    forward(conn, path, "http://cache/adres/")
  end

  match "/contact-info/*path", %{layer: :api, accept: %{json: true}} do
    forward(conn, path, "http://cache/contact-info/")
  end

  match "/persoon/*path", %{layer: :api, accept: %{json: true}} do
    forward(conn, path, "http://cache/persoon/")
  end

  match "/organization/*path", %{layer: :api, accept: %{json: true}} do
    forward(conn, path, "http://cache/organization/")
  end

  match "/agent/*path", %{layer: :api, accept: %{json: true}} do
    forward(conn, path, "http://cache/agent/")
  end

  match "/changeRequest/*path", %{layer: :api, accept: %{json: true}} do
    forward(conn, path, "http://cache/changeRequest/")
  end

  match "/*_path", %{ accept: [:html], layer: :api } do
    Proxy.forward conn, [], "http://frontend/index.html"
  end

  ###############################################################
  # errors
  ###############################################################

  match "/*_path", %{ accept: [:any], layer: :not_found} do
    send_resp( conn, 404, "{\"error\": {\"code\": 404}")
  end
end
